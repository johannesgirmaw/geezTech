from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from commons.utils.model_utils import CommonsModel
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

class Group(CommonsModel):
    name = models.CharField(_("name"), max_length=150, unique=True)
    group_permissions = models.ManyToManyField(
        ContentType, 
        verbose_name=_("group permission"),
        blank = True,
        related_query_name= "group",
        related_name="group_set",
        through = "GroupPermission"
    )

    @property
    def no_of_users(self):
        return CustomUser.objects.filter(groups=self).count()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    id = models.CharField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False, max_length=36)
    middle_name = models.CharField(max_length=200, default="")
    
    user_permissions = models.ManyToManyField(
        ContentType,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="user_set",
        related_query_name="user",
        through = 'UserPermission',
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="user_set",
        related_query_name="user",
    )

    class Meta:
        ordering = ('username', 'first_name', 'last_name')

    def __str__(self):
        return self.first_name

    @property
    def group_permission_list(self):
        return GroupPermission.objects.filter(group__user = self).values('group__name',"content_type__model",'can_view','can_change','can_create','can_delete')
        
    @property
    def user_permission_list(self):
        return UserPermission.objects.filter(user = self).values("content_type__model" ,'can_view','can_change','can_create','can_delete')





class UserPermission(CommonsModel):
    user = models.ForeignKey(CustomUser, verbose_name=_("user"),related_name="user_permission", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, verbose_name=_("content type"), on_delete=models.CASCADE)
    can_view = models.BooleanField(default= False, verbose_name=_("can_views"))
    can_change = models.BooleanField(default= False)
    can_delete = models.BooleanField(default= False)
    can_create = models.BooleanField(default= False)

    def __str__(self):
        return self.user.first_name + " " + self.content_type.model

class GroupPermission(CommonsModel):
    group = models.ForeignKey(Group, verbose_name=_("group"),related_name="group_permission", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, verbose_name=_("content type"), on_delete=models.CASCADE)
    can_view = models.BooleanField(default= False)
    can_change = models.BooleanField(default= False)
    can_delete = models.BooleanField(default= False)
    can_create = models.BooleanField(default= False)

    def __str__(self):
        return self.group.name + " " + self.content_type.model
