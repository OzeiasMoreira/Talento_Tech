import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import make_pipeline

data = {
    'email': [
        'Ganhe dinheiro rápido!!!',
        'Reunião importante amanhã',
        'Oferta exclusiva só hoje',
        'Lembrete: Pagamento da fatura',
        'Você ganhou um prêmio!',
        'Confirmacao de reuniao as 15h',
        'Promoção imperdível!',
        'Reunião de equipe às 10h',
        'Atualização do seu pedido',
        'Convite para evento exclusivo'
    ],
    'label': ['spam', 'não spam', 'spam', 'não spam', 'spam', 'não spam', 'spam', 'não spam', 'não spam', 'spam']
}

df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(df['email'], df['label'], test_size=0.2, random_state=42)

model = make_pipeline(CountVectorizer(), MultinomialNB())

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f'Acurácia: {accuracy_score(y_test, y_pred)}')
print('\nRelatório de Classificação:')
print(classification_report(y_test, y_pred))
print('\nMatriz de Confusão:')
print(confusion_matrix(y_test, y_pred))

def classify_email(model, email):
    prediction = model.predict([email])
    return prediction[0]

spam_email = "Ganhe dinheiro rápido!!!"
legitimate_email = "Reunião importante amanhã às 10h."

spam_prediction = classify_email(model, spam_email)
legitimate_prediction = classify_email(model, legitimate_email)

print(f"E-mail: '{spam_email}' -> Classificação: {spam_prediction}")
print(f"E-mail: '{legitimate_email}' -> Classificação: {legitimate_prediction}")