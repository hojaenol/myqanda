from core.paginations import QandaCursorPagination

class NoticePagination(QandaCursorPagination):
    ordering = '-created_at'
    page_size = 5