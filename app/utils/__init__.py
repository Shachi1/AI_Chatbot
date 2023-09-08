import bcrypt


def generate_hash(value):
    hashed = bcrypt.hashpw(value.encode('utf-8'),  bcrypt.gensalt())
    return hashed.decode('utf-8')


def check_hash(value, hashed):
    result = bcrypt.checkpw(value.encode('utf-8'), hashed.encode('utf-8'))
    return result


def generate_query_model(raw_query):
    queries = {}
    raw_query = str(raw_query.decode('utf-8'))
    raw_queries = raw_query.split('&')
    for query in raw_queries:
        query = query.split('=')
        queries[query[0]] = query[1]

    return queries
