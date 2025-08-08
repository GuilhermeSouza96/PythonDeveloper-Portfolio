from rest_framework.throttling import AnonRateThrottle

class EnrollmentAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'