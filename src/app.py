from fastapi import FastAPI, Request, Path, Response


app = FastAPI()


@app.post("/model/{bedrock_id}/converse")
async def converse_proxy(request: Request, bedrock_id: str = Path()):
    return {"works": True}
