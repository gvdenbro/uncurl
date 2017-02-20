import argparse
import shlex
from collections import OrderedDict
from urllib.parse import parse_qs

import yaml
from six.moves import http_cookies as Cookie

parser = argparse.ArgumentParser()
parser.add_argument('command')
parser.add_argument('url')
parser.add_argument('-d', '--data')
parser.add_argument('-b', '--data-binary', default=None)
parser.add_argument('-H', '--header', action='append', default=[])
parser.add_argument('--compressed', action='store_true')


def parse(curl_command):
    method = "get"

    tokens = shlex.split(curl_command)
    parsed_args = parser.parse_args(tokens)

    post_data = parsed_args.data or parsed_args.data_binary
    query_data = parse_qs(post_data)

    cookie_dict = OrderedDict()
    quoted_headers = OrderedDict()

    for curl_header in parsed_args.header:
        header_key, header_value = curl_header.split(":", 1)

        if header_key.lower() == 'cookie':
            cookie = Cookie.SimpleCookie(header_value)
            for key in cookie:
                cookie_dict[key] = cookie[key].value
        else:
            quoted_headers[header_key] = header_value.strip()

    all = OrderedDict()
    all['url'] = parsed_args.url
    if (len(query_data)):
        all['data'] = OrderedDict({k: flatten(v) for k, v in query_data.items()})
    all['cookies'] = cookie_dict
    all['headers'] = quoted_headers

    result = yaml.dump(all)

    return result


def flatten(list):
    if len(list) == 1:
        return list[0]
    return list
