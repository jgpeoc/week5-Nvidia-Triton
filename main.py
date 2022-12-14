from fastapi import FastAPI
import requests

# Let's generate a new FastAPI app
# Generate a FastAPI instance called `app` with the title 'Triton Health Check'
# https://fastapi.tiangolo.com/
app = FastAPI(title='Triton Model Serving')

#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
@app.get("/", tags=["Health Check"])
async def root():
    return {"face-bokeh" : requests.get(url='http://bokeh:8000').json().get("message"),
            "face-emotion" : requests.get(url='http://emotion:8000').json().get("message"),
            "triton": requests.post(url='http://triton:8000/v2/repository/index').text}