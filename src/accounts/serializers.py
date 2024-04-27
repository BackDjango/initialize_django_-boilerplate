from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label=_("password check")
    )
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label=_("password validation")
    )

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
            "password2",
        ]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("Already use email"))
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": _("Incorrect password.")})
        return data

    def save(self, request):
        user = User(
            email=self.validated_data["email"],
        )

        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def authenticate(self, **options):
        return authenticate(self.context["request"], **options)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if email and password:
            user = authenticate(
                email=email,
                password=password,
            )
            if not user:
                msg = "Incorrect credentials."
                raise serializers.ValidationError(msg, code="authorization")
        attrs["user"] = user
        return attrs
