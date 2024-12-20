from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_analytics.fastapi import Analytics
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from routes import invites
from utils import env

limiter = Limiter(key_func=get_remote_address, default_limits=["30/minute"])
app = FastAPI(title="InviteBlocker API",
              description="InviteBlocker's API to manage blocked invites.",
              version="0.0.1")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

origins = ["*"]

app.include_router(invites.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(Analytics, api_key=env.ANALYTICS_API_KEY)


@app.get("/")
@limiter.exempt
def read_root():
    return {f"InviteBlocker API v{app.version}"}
