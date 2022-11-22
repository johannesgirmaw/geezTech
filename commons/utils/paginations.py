from urllib import response
from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'size_of_page'
    max_page_size = 50
    page_query_param = 'page_number'

    def get_paginated_response(self, data):
        response = Response(data)
        response['count'] = self.page.paginator.count
        response['next'] = self.get_next_link()
        response['previous'] = self.get_previous_link()
        return response


class CustomCursorPagination(pagination.CursorPagination):
    page_size = 2
    ordering = 'category_name'

    def get_ordering(self, request, queryset, view):
        ordering = None
        ordering_filters = [
            filter_cols for filter_cols in getattr(view, 'filter_backends', [])
            if hasattr(filter_cols, 'get_ordering')
        ]

        if ordering_filters:
            filter_cols = ordering_filters[0]
            filter_instance = filter_cols()
            ordering = filter_instance.get_ordering(request, queryset, view)

        if ordering is None:
            ordering = self.ordering
            assert ordering is not None, (
                'Using cursor pagination, but no ordering attribute was declared '
                'on the pagination class.'
            )
            assert '__' not in ordering, (
                'Cursor pagination does not support double underscore lookups '
                'for orderings. Orderings should be an unchanging, unique or '
                'nearly-unique field on the model, such as "-created" or "pk".'
            )

        assert isinstance(ordering, (str, list, tuple)), (
            'Invalid ordering. Expected string or tuple, but got {type}'.format(
                type=type(ordering).__name__
            )
        )

        if isinstance(ordering, str):
            return (ordering,)
        return tuple(ordering)
