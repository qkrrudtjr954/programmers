from collections import defaultdict


def init_db(table):
    db = {
        "JAVA": defaultdict(int),
        "JAVASCRIPT": defaultdict(int),
        "C": defaultdict(int),
        "C++": defaultdict(int),
        "C#": defaultdict(int),
        "SQL": defaultdict(int),
        "PYTHON": defaultdict(int),
        "KOTLIN": defaultdict(int),
        "PHP": defaultdict(int)
    }

    for row in table:
        job, *langs = row.split()
        for score, language in zip(range(len(langs), 0, -1), langs):
            db[language][job] = score

    return db


def solution(table, languages, preference):
    db = init_db(table=table)

    prefer_job = None
    max_prefer_job_score = 0

    for job in ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]:
        prefer_score = sum(db[lang][job] * p for p, lang in zip(preference, languages))

        if prefer_score < max_prefer_job_score:
            continue

        if prefer_score == max_prefer_job_score:
            prefer_job = job if job < prefer_job else prefer_job
        else:
            prefer_job = job

        max_prefer_job_score = prefer_score

    return prefer_job


if __name__ == '__main__':
    print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
                   ["PYTHON", "C++", "SQL"],
                   [7, 5, 5]))
    print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
                   ["JAVA", "JAVASCRIPT"],
                   [7, 5]))
