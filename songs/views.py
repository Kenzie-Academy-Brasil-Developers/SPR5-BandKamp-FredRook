from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from django.shortcuts import get_object_or_404
from .serializers import SongSerializer
from albums.models import Album
from .models import Song


class SongView(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    lookup_url_kwarg = "pk"

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs[self.lookup_url_kwarg])
        serializer.save(album=album)
