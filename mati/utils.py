def validate_data(data, attrs=list()):
    response = True
    for key, value in data.iteritems():
        if key not in attrs:
            response = False
            break

    return response