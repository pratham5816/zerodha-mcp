import uvicorn
from zerodha_mcp.first import loginKite
from zerodha_mcp.server import app


def main() -> None:
    uvicorn.run("zerodha_mcp.server:app", host="127.0.0.1", port=8000, reload=True)


__all__ = ["app", "main", "loginKite"]
