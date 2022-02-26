from .globals import session, request

def get_current_server(session):
    if hasattr(session,"server"):
        return session.server
