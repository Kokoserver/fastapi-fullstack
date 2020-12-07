
from server import app
from server.generalModel import (UserRegister, UserLogin, ChangePassword)
from server.mixin import( hashpassword, checkpassword, getData, Response, mail)
from .model import UserModel
from fastapi import status
PRODUCT_NAME = "Ennebee"




@app.post("/auth/user/register")
async def userRegister(user:UserRegister):
    if user.password1 == user.password2:
        if UserModel.get_user({"email":user.email}):
            return Response({"msg":"Account already exist"}, status.HTTP_401_UNAUTHORIZED)
        password = hashpassword(password=user.password1)
        newUser = UserModel(firstname=user.firstname, lastname=user.lastname, email=user.email, 
        password = password , phone=user.phone)
        newUser.save()
        unactivateUser = UserModel.get_user({"email":user.email})
        if unactivateUser["active"] == False:
            mail(f"http://127.0.0.1:8000/auth/user/{unactivateUser['_id']}/activate", f"{PRODUCT_NAME} Account verification")
        return Response({"msg":"Account has been created succefully, please check your email and activate your account"}, status.HTTP_201_CREATED)
    return Response({"message":"password do not match"}, status.HTTP_400_BAD_REQUEST)

@app.get("/auth/user/{unactivateUser}/activate")
async def UserAvtive(unactivateUser:str):
    user = UserModel.get_user({"_id":unactivateUser})
    if user:
        activated = user["active"]
        if activated == False:
            UserModel.update_user(user, {"active":True})
            mail(f" Welcome to {PRODUCT_NAME} {user['firstname']}, Your account was activated succesfully", F"{PRODUCT_NAME} Account activation")
            return Response({"msg":"Account was activated succesfully"}, status.HTTP_200_OK)
        return Response({"mag":"Account has been activated already"}, status.HTTP_400_BAD_REQUEST)
    return Response({"mag":"Account does not exist"}, status.HTTP_404_NOT_FOUND )


@app.post("/auth/user/login")
async def userLogin(user:UserLogin):
     UserIsFound = UserModel.get_user({"email":user.email})
     if UserIsFound:
        if UserIsFound["active"] == True:
            hashedpassword = UserIsFound["password"]
            checkpass = checkpassword(user.password, hashedpassword)
            if checkpass:
               return UserIsFound
            return Response({"msg":"Password does not match"}, status.HTTP_404_NOT_FOUND)
            if  mail(f"http://127.0.0.1:8000/auth/user/{UserIsFound['_id']}/activate", f"{PRODUCT_NAME} Account verification"):
                return Response({"msg":"Account has not been Activated, An activation link is sent to your email"}, status.HTTP_403_FORBIDDEN)
     return Response({"msg":"Account does not Exist"}, status.HTTP_404_NOT_FOUND)


@app.put("/auth/user/update")
async def userUpdate(user:ChangePassword):
    account = UserModel.get_user({"email":user.email})
    if account:
        if user.password1 == user.password2:
            password = hashpassword(user.password1)
            data = UserModel.update_user(olddata=account, newdata={"password":password})
            return Response({"msg":"password changed successfully"}, code=status.HTTP_200_OK)
        return Response({"msg":"Password does not match"}, code=status.HTTP_404_NOT_FOUND)
    return Response({"msg":"Account does not exist"}, code=status.HTTP_404_NOT_FOUND)


@app.delete("/auth/user/{userid}/delete")
def UserDelete(userid:str):
    user = UserModel.get_user({"_id":userid})
    if user:
        UserModel.remove_user({"_id":userid})
        return Response({"msg":"user have been deleted succesfully"}, status.HTTP_200_OK)
    return Response({"msg":"Account does not exist"}, status.HTTP_404_NOT_FOUND)
    
    
    
    



     

