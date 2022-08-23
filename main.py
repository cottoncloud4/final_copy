import math
import random
import matplotlib.pyplot as plt
import numpy as np


def play(deck, stand, stand_win, stand_loss, stand_draw, hit, hit_win, hit_loss, hit_draw, starting_player_cards):
    random.shuffle(deck)
    cards_dealt = 0
    player_cards = 0
    dealer_cards = 0
    while cards_dealt != 4:
        cards_dealt += 1
        card_drawn = draw()
        if cards_dealt % 2:
            player_cards += card_drawn
        elif not cards_dealt % 2:
            dealer_cards += card_drawn
    starting_player_cards = player_cards
    player_logic = random.randint(0, 1)
    if player_logic == 0:
        stand += 1
        stand_list.append(starting_player_cards)
        while dealer_cards < 17:
            card_drawn = draw()
            dealer_cards += card_drawn
        if player_cards > 21:
            stand_loss += 1
            stand_loss_list.append(starting_player_cards)
        elif dealer_cards > 21:
            stand_win += 1
            stand_win_list.append(starting_player_cards)
        elif player_cards > dealer_cards:
            stand_win += 1
            stand_win_list.append(starting_player_cards)
        elif dealer_cards > player_cards:
            stand_loss += 1
            stand_loss_list.append(starting_player_cards)
        elif player_cards == dealer_cards:
            stand_draw += 1
            stand_draw_list.append(starting_player_cards)
    elif player_logic == 1:
        hit += 1
        hit_list.append(starting_player_cards)
        card_drawn = draw()
        player_cards += card_drawn
        while dealer_cards < 17:
            card_drawn = draw()
            dealer_cards += card_drawn
        if player_cards > 21:
            hit_loss += 1
            hit_loss_list.append(starting_player_cards)
        elif dealer_cards > 21:
            hit_win += 1
            hit_win_list.append(starting_player_cards)
        elif player_cards > dealer_cards:
            hit_win += 1
            hit_win_list.append(starting_player_cards)
        elif dealer_cards > player_cards:
            hit_loss += 1
            hit_loss_list.append(starting_player_cards)
        elif player_cards == dealer_cards:
            hit_draw += 1
            hit_draw_list.append(starting_player_cards)
    deck = 4 * [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    return deck, stand, stand_win, stand_loss, stand_draw, hit, hit_win, hit_loss, hit_draw, starting_player_cards


def draw():
    card_drawn = deck.pop()
    if card_drawn == 'jack' or card_drawn == 'queen' or card_drawn == 'king':
        card_drawn = 10
    elif card_drawn == 'ace':
        card_drawn = 11
    return card_drawn


def list_count(var, number):
    number_of_var = var.count(number)
    return number_of_var


def number_graph():
    x = number_list
    for item in number_list:
        total = starting_player_card_list.count(item)
        temp_graph_list.append(total)
    y = temp_graph_list
    print(x)
    print(y)
    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(4, 22), xticks=np.arange(3, 24),
           ylim=(0, 15000), yticks=np.arange(0, 15001, 1000))
    plt.show()
    temp_graph_list.clear()


def result_graph():
    x = print_list
    y = [hit, hit_win, hit_loss, hit_draw, stand, stand_win, stand_loss, stand_draw]
    print(x)
    print(y)
    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(-1, 8), xticks=np.arange(0, 9),
           ylim=(0, 60000), yticks=np.arange(0, 60001, 15000))
    plt.show()


def graph_number(title):
    x = print_list
    y = temp_graph_list
    fig, ax = plt.subplots()
    print(f'{title}: {temp_graph_list}')
    plt.title(title)
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(-1, 8), xticks=np.arange(0, 9),
           ylim=(0, 6000), yticks=np.arange(0, 6001, 1000))
    plt.show()


def list_number_graph(item):
    for variable in variable_list:
        total = list_count(variable, item)
        temp_graph_list.append(total)
    graph_number(item)
    temp_graph_list.clear()


hit_list, hit_win_list, hit_loss_list, hit_draw_list, stand_list, stand_win_list, stand_loss_list, stand_draw_list, temp_graph_list\
    = [], [], [], [], [], [], [], [], []
hit, hit_win, hit_loss, hit_draw, stand, stand_win, stand_loss, stand_draw, starting_player_cards\
    = 0, 0, 0, 0, 0, 0, 0, 0, 0
deck = 4 * [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
number_list = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
variable_list = [hit_list, hit_win_list, hit_loss_list, hit_draw_list, stand_list, stand_win_list, stand_loss_list, stand_draw_list]
print_list = ['hit', 'hit_w', 'hit_l', 'hit_d', 'stand', 'stand_w', 'stand_l', 'stand_d']

print('Simulating...')
number_of_plays = 0
while number_of_plays != 100000:
    number_of_plays += 1
    deck, stand, stand_win, stand_loss, stand_draw, hit, hit_win, hit_loss, hit_draw, starting_player_cards\
        = play(deck, stand, stand_win, stand_loss, stand_draw, hit, hit_win, hit_loss, hit_draw, starting_player_cards)
starting_player_card_list = hit_list + stand_list

number_graph()
result_graph()
print('number:', print_list)
for item in number_list:
    list_number_graph(item)
