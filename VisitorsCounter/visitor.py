import azure.functions as func

visitor_count = 0

def main(req: func.HttpRequest) -> func.HttpResponse:
    global visitor_count
    visitor_count += 1
    return func.HttpResponse(f"Visitor Count: {visitor_count}", status_code=200)