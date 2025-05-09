from fastapi import FastAPI, Request, Path, Response


app = FastAPI()


@app.post("/bedrock/model/{bedrock_id}/converse")
async def converse_proxy(request: Request, bedrock_id: str = Path()):
    raw_bytes = b'{"ResponseMetadata":{"RequestId":"9a391e1c-c027-4d40-8cec-25751d6117f1","HTTPStatusCode":200,"HTTPHeaders":{"date":"Fri, 09 May 2025 12:27:55 GMT","content-type":"application/json","content-length":"952","connection":"keep-alive","x-amzn-requestid":"9a391e1c-c027-4d40-8cec-25751d6117f1"},"RetryAttempts":0},"output":{"message":{"role":"assistant","content":[{"text":"After reviewing the document, I don\'t see any specific leadership principles outlined for interns. The document is actually a ChatGPT cheat sheet that focuses on prompt engineering techniques, basic structures for prompts, and various use cases for AI in different business functions. It doesn\'t contain information about leadership principles for interns.\\n\\nRegarding the image, I can see a professional portrait of a man in a dark suit with a white shirt and red patterned tie. He has dark hair and is smiling at the camera against a softly blurred background. The image appears to be a corporate or professional headshot, likely for business purposes."}]}},"stopReason":"end_turn","usage":{"inputTokens":2375,"outputTokens":135,"totalTokens":2510},"metrics":{"latencyMs":5310}}'
    return Response(
        content=raw_bytes,
        media_type="application/json",
        status_code=200,
    )
