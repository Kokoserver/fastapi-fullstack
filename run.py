import uvicorn
if __name__ == "__main__":
    uvicorn.run("server:app", reload=True, workers=4, debug=True)