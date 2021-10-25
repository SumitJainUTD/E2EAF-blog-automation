import requests


class ApiClient(object):

    def call_api(self, url, method, data, query_params=None, headers=None,
                 post_params=None, body=None, _preload_content=True,
                 _request_timeout=None):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return requests.get(url,
                                query_params=query_params,
                                _preload_content=_preload_content,
                                _request_timeout=_request_timeout,
                                headers=headers)

        elif method == "HEAD":
            return requests.head(url,
                                 query_params=query_params,
                                 _preload_content=_preload_content,
                                 _request_timeout=_request_timeout,
                                 headers=headers)

        elif method == "OPTIONS":
            return requests.options(url,
                                    query_params=query_params,
                                    headers=headers,
                                    post_params=post_params,
                                    _preload_content=_preload_content,
                                    _request_timeout=_request_timeout,
                                    body=body)
        elif method == "POST":
            return requests.post(url,
                                 query_params=query_params,
                                 headers=headers,
                                 post_params=post_params,
                                 _preload_content=_preload_content,
                                 _request_timeout=_request_timeout,
                                 body=body)
        elif method == "PUT":
            return requests.put(url,
                                query_params=query_params,
                                headers=headers,
                                post_params=post_params,
                                _preload_content=_preload_content,
                                _request_timeout=_request_timeout,
                                body=body)
        elif method == "PATCH":
            return requests.patch(url,
                                  query_params=query_params,
                                  headers=headers,
                                  post_params=post_params,
                                  _preload_content=_preload_content,
                                  _request_timeout=_request_timeout,
                                  body=body)
        elif method == "DELETE":
            return requests.delete(url,
                                   query_params=query_params,
                                   headers=headers,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body)
        else:
            raise ValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )