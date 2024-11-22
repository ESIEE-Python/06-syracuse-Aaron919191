from tkinter.messagebox import ERROR
from plotly.graph_objects import Scatter, Figure

def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({'layout': {'title': {'text': title},
                             'xaxis': {'title': {'text': "Étape"}},
                             'yaxis': {'title': {'text': "Valeur"}},
                             }
                  })
    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker=dict(color="blue"))
    fig.add_trace(t)
    fig.show()

def syracuse_l(n):
    """Retourne la suite de Syracuse de source n

        Args:
            n (int): la source de la suite

        Returns:
            list: la suite de Syracuse de source n
        """
    if n <= 0:
        print("La valeur de n doit être un entier positif.")
        return ERROR
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

        Args:
            l (list): la suite de Syracuse

        Returns:
            int: le temps de vol
        """
    return len(l) - 1

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

        Args:
            l (list): la suite de Syracuse

        Returns:
            int: le temps de vol en altitude
        """
    temp = 0
    for valeur in l:
        if valeur > l[0]:
            temp = temp + 1
    return temp - 1

def altitude_maximale(l):
    """Retourne l'altitude maximale d'une suite de Syracuse

        Args:
            l (list): la suite de Syracuse

        Returns:
            int: l'altitude maximale
        """
    return max(l)

def main():
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print("Temps de vol :", temps_de_vol(lsyr))
    print("Temps de vol en altitude :", temps_de_vol_en_altitude(lsyr))
    print("Altitude maximale :", altitude_maximale(lsyr))

if __name__ == "__main__":
    main()