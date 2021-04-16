import pickle


if __name__ == "__main__":
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # model.predict_proba(y)
