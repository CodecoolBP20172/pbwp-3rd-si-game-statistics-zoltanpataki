import operator


def file_opening(file_name="game_stat.txt"):
    game_list = []
    with open(file_name, 'r') as inputfile:
        for line in inputfile:
            game_list.append(line.strip().split('\t'))
    return game_list


def get_most_played(file_name="game_stat.txt"):
    sold_list = []
    title_list = []
    for game in file_opening(file_name):
            sold_list.append(float(game[1]))
            title_list.append(game[0])
    return title_list[(sold_list.index(max(sold_list)))]


def sum_sold(file_name="game_stat.txt"):
    sold_list = []
    for game in file_opening(file_name):
        sold_list.append(float(game[1]))
    return sum(sold_list)


def get_selling_avg(file_name="game_stat.txt"):
    sold_list = []
    for game in file_opening(file_name):
        sold_list.append(float(game[1]))
    return sum(sold_list)/len(sold_list)


def count_longest_title(file_name="game_stat.txt"):
    title_list = []
    for game in file_opening(file_name):
        title_list.append(len(game[0]))
    return max(title_list)


def get_date_avg(file_name="game_stat.txt"):
    year_list = []
    for game in file_opening(file_name):
        year_list.append(int(game[2]))
    return round(sum(year_list)/len(year_list))


def get_game(file_name, title):
    properties_list = []
    for game in file_opening(file_name):
        if title in game:
            for properties in game:
                properties_list.append(properties)
    properties_list[1] = float(properties_list[1])
    properties_list[2] = int(properties_list[2])
    return properties_list


def count_grouped_by_genre(file_name="game_stat.txt"):
    genre_list = []
    technical_list = []
    count_list = []
    for game in file_opening(file_name):
        technical_list.append(game[3])
        if game[3] not in genre_list:
            genre_list.append(game[3])
    i = 0
    for genre in genre_list:
        count_list.append(technical_list.count(genre_list[i]))
        i += 1
    genre_dict = dict(zip(genre_list, count_list))
    return genre_dict


def get_date_ordered(file_name="game_stat.txt"):
    year_list = []
    title_list = []
    for game in file_opening(file_name):
        year_list.append(game[2])
        title_list.append(game[0])
    date_dict = dict(zip(title_list, year_list))
    sorted_date_list = sorted(date_dict.items(), key=operator.itemgetter(1), reverse=True)
    final_list = []
    for item in sorted_date_list:
        i = 0
        while i <= len(sorted_date_list)-2:
            if sorted_date_list[i][1] == sorted_date_list[i+1][1] and sorted_date_list[i][0] > sorted_date_list[i+1][0]:
                temp = sorted_date_list[i]
                sorted_date_list[i] = sorted_date_list[i+1]
                sorted_date_list[i+1] = temp
            else:
                i += 1
        final_list.append(item[0])
    return final_list