def file_opening(file_name):
    game_list = []
    with open(file_name, 'r') as inputfile:
        for line in inputfile:
            game_list.append(line.strip().split('\t'))
    return game_list


def count_games(file_name):
    return len(file_opening(file_name))


def decide(file_name, year):
    for game in file_opening(file_name):
        for data in game:
            if str(year) in game:
                return True
                break
    return False


def get_latest(file_name):
    year = []
    for game in file_opening(file_name):
        year.append(game[2])
    return file_opening(file_name)[year.index(max(year))][0]


def count_by_genre(file_name, genre):
    number_by_genre = 0
    for game in file_opening(file_name):
        if genre in game:
            number_by_genre += 1
    return number_by_genre


def get_line_number_by_title(file_name, title):
        for number, game in enumerate(file_opening(file_name)):
            if title in game:
                return number+1
        raise ValueError


def sort_abc(file_name):
    title_list = []
    for game in file_opening(file_name):
        title_list.append(game[0])
    iteration = 1
    while iteration < len(title_list):
        j = 0
        while j <= len(title_list)-2:
            if title_list[j] > title_list[j+1]:
                temp = title_list[j]
                title_list[j] = title_list[j+1]
                title_list[j+1] = temp
            else:
                j += 1
        iteration += 1
    return title_list


def get_genres(file_name):
    genre_list = []
    for game in file_opening(file_name):
        if game[3] not in genre_list:
            genre_list.append(game[3])
    return sorted(genre_list, key=lambda v: v.lower())


def when_was_top_sold_fps(file_name):
    sold_list = []
    year_list = []
    for game in file_opening(file_name):
        if "First-person shooter" in game:
            sold_list.append(float(game[1]))
            year_list.append(int(game[2]))
    return year_list[(sold_list.index(max(sold_list)))]