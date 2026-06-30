def check_gap(results):

    documents = results.get("documents", [])

    if not documents:
        return True

    if len(documents[0]) == 0:
        return True

    return False