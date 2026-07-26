import pandas as pd

def fetch_report(report_type: str):
    # Simulate processing 1M+ rows
    data = pd.DataFrame({"metric": range(1, 1000001)})
    if report_type == "summary":
        return {"rows": len(data), "mean": data["metric"].mean()}
    elif report_type == "max":
        return {"max": data["metric"].max()}
    else:
        return {"message": "Unknown report type"}
