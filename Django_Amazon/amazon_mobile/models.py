from django.db import models
from djmoney.models.fields import MoneyField

sim_choices = (
    ("SIM1", "SIM1"),
    ("SIM2", "SIM2"),
)
colors_choices = (
    ("Black", "Black"),
    ("Grey", "Grey"),
    ("Blue", "Blue"),
    ("Gold", "Gold"),
    ("Rose Gold", "Rose Gold"),
)


class Mobile_Technology(models.Model):
    technology_name = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.technology_name)


# Create your models here.
class Amazon_Mobile(models.Model):
    amazon_seller = models.ForeignKey('amazon_seller.Amazon_Seller', on_delete=models.CASCADE, null=True, blank=True)
    mobile_name = models.CharField(max_length=100)
    mobile_technology = models.ForeignKey("amazon_mobile.mobile_technology", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['mobile_technology']

    def __str__(self):
        return '%d:' % (self.mobile_name)


    # network_technology = models.
    # launch_announced = models.DateTimeField
    # launch_status = models.CharField(max_length=200)
    # body_dimensions = models.CharField(max_length=200)
    # body_weight = models.IntegerField(default=0)
    # body_build = models.CharField(max_length=200)
    # body_sim = models.CharField(max_length=100, choices=sim_choices)
    # display_type = models.CharField(max_length=200)
    # display_size = models.IntegerField(default=0)
    # display_resolution = models.IntegerField(default=0)
    # platform_os = models.CharField(max_length=200)
    # platform_chipset = models.CharField(max_length=200)
    # platform_cpu = models.CharField(max_length=200)
    # platform_gpu = models.CharField(max_length=200)
    # memory_card_slot = models.CharField(max_length=100)
    # memory_internal = models.CharField(max_length=100)
    # main_camera_dual = models.IntegerField(default=0)
    # main_camera_features = models.CharField(max_length=100)
    # main_camera_video = models.CharField(max_length=200)  # video field
    # selfie_camera_single = models.CharField(max_length=100)
    # selfie_camera_video = models.CharField(max_length=100)
    # # selfie_camera_Image = models.ImageField((upload_to ="media/Amazon_Mobile/selfie_camera_Image")
    # # sound_loudspeaker=models.BooleanField(default=True)
    # comms_wlan = models.CharField(max_length=100)
    # comms_bluetooth = models.IntegerField(default=0)
    # comms_gps = models.CharField(max_length=100)
    # comm_nfc = models.BooleanField(default=True)
    # comm_radio = models.CharField(max_length=100)
    # comm_usb = models.CharField(max_length=100)
    # features_sensors = models.ImageField()
    # battery_type = models.CharField(max_length=100)
    # misc_colors = models.CharField(max_length=100, choices=colors_choices)
    # misc_models = models.CharField(max_length=100)
    # mise_sar = models.CharField(max_length=100)
    # misc_price = MoneyField(default=0, default_currency='INR', max_digits=11, null=True, blank=True)
    # tests_performance = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.mobile_name)
