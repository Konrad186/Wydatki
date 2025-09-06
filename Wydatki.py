#Program umożliwia użytkownikowi wprowadzanie wydatków, zarządzanie nimi oraz wizualizację danych w postaci wykresu.

import matplotlib.pyplot as plt

# Klasa pierwsza: Pobieranie i walidacja danych
class WprowadzanieDanych:
    liczba_obiektow = 0  # Pole klasy, licznik obiektów

    def __init__(self):
        self._wydatki = {}
        WprowadzanieDanych.liczba_obiektow += 1  # Inkrementacja przy każdym utworzeniu obiektu

    def dodaj_wydatek(self):
        """Metoda dodająca wydatek od użytkownika z walidacją danych."""
        while True:
            try:
                kategoria = input("Podaj kategorię wydatku (np. jedzenie, picie, rozrywka, transport): ").strip()
                if not kategoria.isalpha():
                    raise ValueError("Kategoria musi zawierać tylko litery.")
                kwota = float(input(f"Podaj kwotę dla kategorii '{kategoria}': "))
                if kwota < 0:
                    raise ValueError("Kwota nie może być ujemna.")
                self._wydatki[kategoria] = self._wydatki.get(kategoria, 0) + kwota
                break
            except ValueError as e:
                print(f"Błąd: {e}. Spróbuj ponownie.")

    def pobierz_wydatki(self):
        """Getter zwracający słownik wydatków."""
        return self._wydatki


# Klasa druga: Zarządzanie i przetwarzanie danych
class ZarzadzanieWydatkami:
    def __init__(self, wydatki):
        """Konstruktor inicjalizujący dane."""
        self._wydatki = wydatki

    @property
    def wydatki(self):
        """Getter dla wydatków."""
        return self._wydatki

    @wydatki.setter
    def wydatki(self, nowe_wydatki):
        """Setter dla wydatków."""
        if not isinstance(nowe_wydatki, dict):
            raise ValueError("Dane muszą być w formacie słownika.")
        self._wydatki = nowe_wydatki

    def wyswietl_wydatki(self):
        """Wyświetla wydatki w formacie tekstowym."""
        print("\nTwoje wydatki:")
        for kategoria, kwota in self._wydatki.items():
            print(f"- {kategoria}: {kwota:.2f} zł")
        print(f"Łączna kwota wydatków: {self.suma_wydatkow():.2f} zł")

    def suma_wydatkow(self):
        """Zwraca sumę wszystkich wydatków."""
        return sum(self._wydatki.values())


# Klasa trzecia: Wizualizacja danych
class RysowanieWykresu:
    def __init__(self, wydatki):
        """Konstruktor inicjalizujący dane do wykresu."""
        self.wydatki = wydatki

    def rysuj_wykres(self):
        """Tworzy wykres słupkowy na podstawie wydatków."""
        kategorie = list(self.wydatki.keys())
        kwoty = list(self.wydatki.values())

        plt.bar(kategorie, kwoty, color='skyblue')
        plt.xlabel("Kategoria")
        plt.ylabel("Kwota (zł)")
        plt.title("Wydatki według kategorii")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


# Główna część programu
if __name__ == "__main__":
    # Tworzenie obiektu klasy pierwszej
    wprowadzanie_danych = WprowadzanieDanych()

    # Wprowadzanie danych od użytkownika
    print("Wprowadzanie wydatków (wpisz 'stop', aby zakończyć):")
    while True:
        user_input = input("Czy chcesz dodać wydatek? (tak/stop): ").strip().lower()
        if user_input == "stop":
            break
        elif user_input == "tak":
            wprowadzanie_danych.dodaj_wydatek()
        else:
            print("Nieprawidłowa odpowiedź. Wpisz 'tak' lub 'stop'.")

    # Tworzenie obiektu klasy drugiej
    wydatki = wprowadzanie_danych.pobierz_wydatki()
    zarzadzanie_wydatkami = ZarzadzanieWydatkami(wydatki)

    # Wyświetlanie danych
    zarzadzanie_wydatkami.wyswietl_wydatki()

    # Tworzenie obiektu klasy trzeciej i generowanie wykresu
    rysowanie_wykresu = RysowanieWykresu(wydatki)
    rysowanie_wykresu.rysuj_wykres()

    # Wyświetlanie liczby obiektów klasy pierwszej
    print(f"Liczba obiektów klasy WprowadzanieDanych: {WprowadzanieDanych.liczba_obiektow}")
