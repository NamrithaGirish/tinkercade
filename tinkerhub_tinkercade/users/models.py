from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db.models import CharField, BooleanField, TextChoices, URLField, IntegerField

class User(AbstractUser):
    """
    Default custom user model for tinkerhub_tinkercade.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]
    profile_image = URLField(max_length=3000, null=True, blank=True)
    points = IntegerField(default=30, null=True, blank=True)

    class UserType(TextChoices):
        PARTICIPANTS = "P", _("Participants")
        CORDS = "C", _("Coordinator")
        VOLUNTEER = "V", _("Volunteer")
        ADMIN = "A", _("Admin")

    user_type = CharField(
        max_length=1,
        choices=UserType.choices,
        default=UserType.PARTICIPANTS,
    )
    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
    def __str__(self):
        return self.email
    class Meta:
        ordering = ["-email"]
