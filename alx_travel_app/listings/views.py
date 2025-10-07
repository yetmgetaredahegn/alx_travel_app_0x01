from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Listings.
    Provides list, create, retrieve, update, delete.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Bookings.
    Provides list, create, retrieve, update, delete.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
