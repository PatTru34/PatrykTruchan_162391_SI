import gradio as gr
import pandas as pd


def main(plik, n, zapytania):
    df = pd.read_csv(plik)
    df.dropna(axis=0, inplace=True)
    df = df.head(int(n))
    atryb = df.shape
    klasdec = df.iloc[:, -1].value_counts()

    if zapytania == "":
        zapytanie="Ogólne informacje"
        wynik = f"Liczba atrybutow: {atryb[1]}", f"Liczba obiektow: {atryb[1] * atryb[0]}"
        return zapytanie, df, wynik

    if zapytania == "a" or zapytania=="Ile klas decyzyjnych":
        zapytanie = f"Ile klas decyzyjnych"
        wynik = f"Ilość klas decyzyjnych: {len(klasdec)}"
        return zapytanie, df, wynik

    if zapytania == "b" or zapytania=="Wielkość każdej klasy decyzyjnej":
        zapytanie = "Wielkość każdej klasy decyzyjnej"
        wynik = f"Wielkości klas decyzyjnych: {klasdec.to_dict()}"
        return zapytanie, df, wynik
    else:
        zapytanie = "Nie przewidziane zapytanie"
        wynik = "Nie potrafię na nie odpowiedzieć"
        return zapytanie, df, wynik


gr.Interface(main,
             inputs = [gr.Textbox(label="Nazwa pliku"),
          gr.Number(label="Liczba wierszy"),
          gr.inputs.Textbox(label="Wybierz zapytanie: a: Ile klas decyzyjnych, b: Wielkość każdej klasy decyzyjnej")],
             outputs = [gr.outputs.Textbox(label="Zapytanie"),
           gr.outputs.Dataframe(label="Tabela", type='pandas'),
           gr.outputs.Textbox(label="Wynik")]).launch()