from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    """Detecta anomalias usando Isolation Forest"""
    model = IsolationForest()
    model.fit(data)
    predictions = model.predict(data)
    anomalies = [data[i] for i in range(len(predictions)) if predictions[i] == -1]
    return anomalies
