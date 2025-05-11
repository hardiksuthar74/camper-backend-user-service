import uvicorn


def main():
    uvicorn.run(
        app="app.server:app",
        reload=True,
        workers=1,
    )


if __name__ == "__main__":
    main()
