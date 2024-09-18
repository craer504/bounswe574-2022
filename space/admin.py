from django.contrib import admin
from space.models import SpaceModel, MessageModel, StepModel, TermModel, ResourceModel, ExtendedUser
from space.models.step import StepModel

@admin.register(SpaceModel)
class SpaceAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'created_date', 'member_list')
    search_fields=('title', 'content')
    list_filter=['created_date']

@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    list_display=('sender', 'memberspace', 'message', 'created_time')
    search_fields=('sender__username',)   


@admin.register(StepModel)
class StepAdmin(admin.ModelAdmin):
    list_display=('stepspace', 'steptitle', 'stepcontent', 'relatedresource', 'stepcreator', 'created_time')
    search_fields=('steptitle', 'stepcontent')   

@admin.register(TermModel)
class TermAdmin(admin.ModelAdmin):
    list_display=('termwriter', 'termspace', 'termtitle', 'termstep', 'created_time')
    search_fields=('termtitle', 'termdefinition')   

@admin.register(ResourceModel)
class ReourceAdmin(admin.ModelAdmin):
    list_display=('resourcespace', 'resourcename', 'resourceinfo', 'resourceattachment', 'resourcecreator', 'created_time')
    search_fields=('resourcename', 'resourceinfo')

@admin.register(ExtendedUser)
class ExtendedUserAdmin(admin.ModelAdmin):
    list_display=('interest', 'extendeduser')
    search_fields=('interest',)