SUPERUSER = 1
STAFF = 2
DRIVER = 3
CLIENT = 4

USER_TYPE_CHOICES = (
      (SUPERUSER, 'superuser'),
      (STAFF, 'staff'),
      (DRIVER, 'driver'),
      (CLIENT, 'client'),
  )

VEHICLE_CAPACITY_UNIT_CHOICES = (
        ('kg', 'kg'),
        ('ton', 'ton'),
        ('m3', 'm3'),
        ('l', 'l'),
        ('cm3', 'cm3'),
)

WEIGHT_UNIT_CHOICES = (
        ('kg', 'kg'),
        ('ton', 'ton'),
    )

VOLUME_UNIT_CHOICES = (
        ('m3', 'm3'),
        ('l', 'l'),
)