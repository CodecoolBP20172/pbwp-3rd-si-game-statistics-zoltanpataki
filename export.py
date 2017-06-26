import reports


def export_reports_answers(file_name, title, year, genre, export_file="export_reports.txt"):
    file = open(export_file, "w")
    file.write("The number of games in the file: {}\n".format(reports.count_games(file_name)))
    file.write("There is a game from a given year: {}\n".format(reports.decide(file_name, year)))
    file.write("The latest game is: {}\n".format(reports.get_latest(file_name)))
    file.write("The number of games we have by the given genre: {}\n".format(reports.count_by_genre(file_name, genre)))
    file.write("The line number of the given game is: {}\n".format(reports.get_line_number_by_title(file_name, title)))
    file.write("The alphabetical ordered list of the titles is: {}\n".format(reports.sort_abc(file_name)))
    file.write("The genres are: {}\n".format(reports.get_genres(file_name)))
    file.write("The release date of the top sold First-person shooter game is: {}\n".format(reports.when_was_top_sold_fps(file_name)))
    file.close()

export_reports_answers("game_stat.txt", "Terraria", 2004, "First-person shooter")
