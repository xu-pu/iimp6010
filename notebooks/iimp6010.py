# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:58:01 2020

@author: terry
"""

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import random
from copy import deepcopy


class City:
    graph = g = nx.Graph()
    node_positions = []
    building_nodes = []
    edges = []  # only used in generate_city()
    nodes = []  # only used in generate_city()


def generate_city():
    node_prob = 0.2
    building_prob = 0.2

    edgelist = pd.read_csv('data/edge.csv')
    nodelist = pd.read_csv('data/nodes.csv')

    g = nx.Graph()

    for i, element in edgelist.iterrows():
        g.add_edge(element[0], element[1], weight=random.randint(5, 50), color=element[3])

    for i, element in nodelist.iterrows():
        g.nodes[element['id']].update(element[1:].to_dict())

    # delete some nodes randomly
    for node in list(g.nodes):
        if node == 'n00' or node == 'n44':
            continue
        else:
            if random.random() < node_prob:
                t = deepcopy(g)
                t.remove_node(node)
                if nx.is_connected(t):
                    g.remove_node(node)
                t.clear()

    x_coor = []
    y_coor = []

    for node in list(g.nodes):
        x_coor.append(g.nodes[node]['x'])
        y_coor.append(g.nodes[node]['y'])

    nodemap = {'id': list(g.nodes), 'x': x_coor, 'y': y_coor}

    # add buildings randomly
    building_nodes = []
    i = 1
    for node in list(g.nodes):
        dic = {}
        if g.nodes[node]['x'] == 0 or g.nodes[node]['x'] == 900 or g.nodes[node]['y'] == 0 or g.nodes[node]['y'] == 900:
            continue
        else:
            if random.random() < building_prob or i == 0:
                dic['id'] = chr(ord('@') + i)
                dic['x'] = g.nodes[node]['x'] + 50
                dic['y'] = g.nodes[node]['y']
                building_nodes.append(dic)
                i = i + 1

                g.add_node(dic['id'], x=dic['x'], y=dic['y'], height=random.randint(5, 20))
                g.add_edge(node, dic['id'], weight=random.randint(5, 50), color='black')

                adj_node = [x for x, y in g.nodes(data=True) if y['x'] == g.nodes[node]['x'] + 100 and y['y'] == g.nodes[node]['y']]
                for n in adj_node:
                    g.remove_edge(node, n)
                    g.add_edge(n, dic['id'], weight=random.randint(5, 50), color='black')

    build_id = []
    build_x = []
    build_y = []
    for build in building_nodes:
        build_id.append(build['id'])
        build_x.append(build['x'])
        build_y.append(build['y'])

    building = {'id': build_id, 'x': build_x, 'y': build_y}

    buildingnodes = pd.DataFrame(building, columns=['id', 'x', 'y'])

    edgenode = []
    weight = []
    for edge in list(g.edges):
        edgenode.append(edge)
        weight.append(g.edges[edge]['weight'])

    left = []
    right = []

    for item in edgenode:
        left.append(item[0])
        right.append(item[1])

    edgenodes = {'node1': left, 'node2': right, 'weight': weight}

    ednodes = pd.DataFrame(edgenodes, columns=['node1', 'node2', 'weight'])

    city = City()
    city.building_nodes = buildingnodes
    city.edges = ednodes
    city.nodes = pd.DataFrame(nodemap, columns=['id', 'x', 'y'])
    city.graph = g
    return city


def save_city_to_file(city):
    city.edges.to_csv('data/random_edges.csv', index=False)
    city.building_nodes.to_csv('data/building_nodes.csv', index=False)
    city.nodes.to_csv('data/random_nodes.csv', index=False)


def load_city():
    edgelist = pd.read_csv('data/random_edges.csv')
    nodelist = pd.read_csv('data/random_nodes.csv')
    buildingnode = pd.read_csv('data/building_nodes.csv')

    g = nx.Graph()

    for i, element in edgelist.iterrows():
        g.add_edge(element[0], element[1], weight=element[2])

    for i, element in nodelist.iterrows():
        g.nodes[element['id']].update(element[1:].to_dict())

    building_nodes = []
    for i, element in buildingnode.iterrows():
        g.nodes[element['id']].update(element[1:].to_dict())
        dic = {'id': element['id'], 'x': element['x'], 'y': element['y']}
        building_nodes.append(dic)

    city = City()
    city.graph = g
    city.building_nodes = building_nodes
    city.node_positions = {node[0]: (node[1]['x'], node[1]['y']) for node in city.graph.nodes(data=True)}

    return city


def visualize_city(city):
    fig = plt.figure(dpi=200, figsize=[10, 10])
    ax = fig.add_subplot(111)
    draw_city_on_axes(city, ax)
    plt.axis('square')
    plt.show()


def draw_city_on_axes(city,ax):
    number_id = 0
    for build in city.building_nodes:
        number_id = number_id + 1
        draw_x = [build['x'], build['x']]
        draw_y = [build['y'], build['y'] - 20]
        ax.add_patch(plt.Rectangle((build['x'] - 30, build['y'] - 80), 60, 60, edgecolor='black', facecolor='none'))
        plt.plot(draw_x, draw_y, color='blue', linewidth=1, alpha=0.2)
        plt.text(build['x'], build['y'] - 50, chr(ord('@') + number_id), horizontalalignment='center', verticalalignment='center', fontsize=15, color='blue')
    #node_positions = {node[0]: (node[1]['x'], node[1]['y']) for node in city.graph.nodes(data=True)}
    label_positions = {node[0]: (node[1]['x'] - 15, node[1]['y'] + 10) for node in city.graph.nodes(data=True)}
    node_labels = {}
    for node in city.graph.nodes(data=True):
        node_labels.update({node[0]: node[0]})
    nx.draw_networkx_nodes(city.graph, pos=city.node_positions, node_size=10, node_color='black', alpha=0.2, ax=ax)
    nx.draw_networkx_labels(city.graph, pos=label_positions, labels=node_labels, font_size=8, font_color='black', horizontalalignment='center', verticalalignment='center', ax=ax)
    nx.draw_networkx_edges(city.graph, pos=city.node_positions, edge_color='blue', alpha=0.2, ax=ax)


def visualize_path_in_city(city, path):
    fig = plt.figure(dpi=200, figsize=[10, 10])
    ax = fig.add_subplot(111)
    draw_city_on_axes(city, ax)
    shortest_path_list = []
    for i in range(len(path) - 1):
        shortest_path_list.append([path[i], path[i + 1]])
    nx.draw_networkx_edges(city.graph, pos=city.node_positions, edgelist=shortest_path_list, edge_color='r', ax=ax, width=5)
    plt.axis('square')
    plt.show()


if __name__ == "__main__":
    #my_city = generate_city()
    #save_city_to_file(my_city)
    my_city = load_city()
    visualize_city(my_city)
    p = nx.shortest_path(my_city.graph,'A','B')
    visualize_path_in_city(my_city,p)
