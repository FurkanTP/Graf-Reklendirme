#FURKAN TOP B201200372 Renklendirme Graf
colors = ["mavi", "turuncu", "krımızı", "yeşil"]
states = ['Edirne', 'Kırklareli', 'Tekirdağ', 'Çanakkale','İstanbul', 'Balıkesir', 'Bursa', 'Yalova', 'Sakarya', 'Bilecik', 'Kocaeli']

neighbors = {}

neighbors['Bursa'] = ['Yalova', 'Kocaeli', 'Sakarya', 'Balıkesir', 'Bilecik']   #deg(B)=5
neighbors['Kocaeli'] = ['Yalova', 'Sakarya', 'İstanbul', 'Bursa']               #deg(K)=4
neighbors['Tekirdağ'] = ['Edirne', 'Kırklareli', 'Çanakkale', 'İstanbul']       #deg(T)=4
neighbors['Çanakkale'] = ['Edirne', 'Tekirdağ', 'Balıkesir']                    #deg(Ç)=3
neighbors['Edirne'] = ['Kırklareli', 'Tekirdağ', 'Çanakkale']                   #deg(E)=3
neighbors['İstanbul'] = ['Tekirdağ', 'Kocaeli', 'Kırklareli']                   #deg(İ)=3
neighbors['Kırklareli'] = ['Edirne', 'Tekirdağ', 'İstanbul']                    #deg(K)=3
neighbors['Sakarya'] = ['Bursa', 'Kocaeli', 'Bilecik']                          #deg(S)=3
neighbors['Balıkesir'] = ['Çanakkale', 'Bursa']                                 #deg(B)=2
neighbors['Bilecik'] = ['Bursa', 'Sakarya']                                     #deg(B)=2       
neighbors['Yalova'] = ['Bursa', 'Kocaeli']                                      #deg(Y)=2


colors_of_states = {}


def promising(state, color):
    for neighbor in neighbors.get(state):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True


def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color


def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
    print(colors_of_states)

   
main()

