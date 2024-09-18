from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import MessageModel, SpaceModel, ContentModel, RelationModel, StepModel, TermModel, ResourceModel, ActivityStreamModel
from quiz.models import QuizModel
import json
from datetime import datetime


class MyActivity:

    def __init__(self, context, summary, type, actor, object, published):
        self.context = context
        self.summary = summary
        self.type = type
        self.actor = actor
        self.object = object
        self.published = published

    # content ---> olayın gerçekleştiği space'in ismi
    # summary ---> olayın özeti
    # type ---> olayın çeşidi
    # actor ---> olayı gerçekleştiren kişi
    # object ---> olaydaki nesne
    # published ---> olayın gerçekleştiği tarih

    def dict_creator(self):
        activity_dict = {
            'context': self.context,
            'summary': self.summary,
            'type': self.type,
            'actor': self.actor,
            'object': self.object,
            'published': self.published,
        }
        return activity_dict

    # gerek kalmadı
    def json_creator(activity_dict):
        activity_json = json.dumps(activity_dict)
        return activity_json

    # gerek kalmadı
    def json_loader(activity):
        parsed_data = json.loads(activity)
        return parsed_data


# "Save" veya "Create" aksiyonları - db'ye bir şey eklenince tetiklenecekler:


@receiver(post_save, sender=MessageModel)
def on_create_message(sender, instance, **kwargs):

    msg_activity = MyActivity(
        context=instance.memberspace.title,
        summary=f"User '{instance.sender.username}' posted a message in the space '{instance.memberspace.title}', on '{datetime.today().strftime('%d/%m/%Y, %H:%M:%S')}'",
        type='post_message',
        actor=instance.sender.username,
        object=instance.message,
        #published=instance.created_time.strftime('%d/%m/%Y, %H:%M:%S'),
        published=datetime.today().strftime('%d/%m/%Y, %H:%M:%S'),
    )

    activity_data_json = msg_activity.dict_creator()

    ActivityStreamModel.objects.create(activity=activity_data_json)

    print(activity_data_json)


@receiver(post_save, sender=SpaceModel)
def on_create_space(sender, instance, **kwargs):

    crt_spc_activity = MyActivity(
        context=instance.title,
        summary=f"User '{instance.author.username}' created a space named '{instance.title}', on '{datetime.today().strftime('%d/%m/%Y, %H:%M:%S')}'",
        type='create_space',
        actor=instance.author.username,
        object=instance.content,
        #published=instance.created_date.strftime('%d/%m/%Y, %H:%M:%S'),
        published=datetime.today().strftime('%d/%m/%Y, %H:%M:%S'),
    )

    activity_data_json = crt_spc_activity.dict_creator()

    ActivityStreamModel.objects.create(activity=activity_data_json)

    print(activity_data_json)


@receiver(post_save, sender=ContentModel)
def on_create_content(sender, instance, **kwargs):

    crt_cntnt_activity = MyActivity(
        context=instance.space.title,
        summary=f"User '{instance.creator.username}' created a content named '{instance.title}' in '{instance.space.title}', on {datetime.today().strftime('%d/%m/%Y, %H:%M:%S')}",
        type='create_content',
        actor=instance.creator.username,
        object=instance.link,
        #published=instance.created_time.strftime('%d/%m/%Y, %H:%M:%S'),
        published=datetime.today().strftime('%d/%m/%Y, %H:%M:%S'),
    )

    activity_data_json = crt_cntnt_activity.dict_creator()

    ActivityStreamModel.objects.create(activity=activity_data_json)

    print(activity_data_json)


@receiver(post_save, sender=RelationModel)
def on_create_relation(sender, instance, **kwargs):

    crt_rltn_activity = MyActivity(
        context=instance.space.title,
        summary=f"User '{instance.creator.username}' created a relation named '{instance.target_content.title}' connecting '{instance.source_content.title}' and '{instance.target_content.title}' in '{instance.space.title}', on {datetime.today().strftime('%d/%m/%Y, %H:%M:%S')}",
        type='create_relation',
        actor=instance.creator.username,
        object={
            'source_content': instance.source_content.title,
            'target_content': instance.target_content.title,
        },
        #published=instance.created_time.strftime('%d/%m/%Y, %H:%M:%S'),
        published=datetime.today().strftime('%d/%m/%Y, %H:%M:%S'),
    )

    activity_data_json = crt_rltn_activity.dict_creator()

    ActivityStreamModel.objects.create(activity=activity_data_json)

    print(activity_data_json)


@receiver(post_save, sender=StepModel)
def on_create_step(sender, instance, **kwargs):

    crt_stp_activity = MyActivity(
        context=instance.stepspace.title,
        summary=f"User '{instance.stepcreator.username}' created a step named '{instance.steptitle}' in the space '{instance.stepspace.title}', on '{datetime.today().strftime('%d/%m/%Y, %H:%M:%S')}'",
        type='create_step',
        actor=instance.stepcreator.username,
        object=instance.stepcontent,
        #published=instance.created_time.strftime('%d/%m/%Y, %H:%M:%S'),
        published=datetime.today().strftime('%d/%m/%Y, %H:%M:%S'),
    )

    activity_data_json = crt_stp_activity.dict_creator()

    ActivityStreamModel.objects.create(activity=activity_data_json)

    print(activity_data_json)


@receiver(post_save, sender=TermModel)
def on_create_term(sender, instance, **kwargs):

    crt_trm_activity = MyActivity(
        context=instance.termspace.title,
        summary=f"User '{instance.termwriter.username}' created a term named '{instance.termtitle}' in the space '{instance.termspace.title}', on {instance.created_time.strftime('%d/%m/%Y, %H:%M:%S')}",
        type='create_term',
        actor=instance.termwriter.username,
        object={
            'term_definition': instance.termdefinition,
            'term_step': instance.termstep,
        },
        #published=instance.created_time.strftime('%d/%m/%Y, %H:%M:%S'),
        published=datetime.today().strftime('%d/%m/%Y, %H:%M:%S'),
    )

    activity_data_json = crt_trm_activity.dict_creator()

    ActivityStreamModel.objects.create(activity=activity_data_json)

    print(activity_data_json)


@receiver(post_save, sender=QuizModel)
def on_create_quiz(sender, instance, **kwargs):

    crt_qz_activity = MyActivity(
        context=instance.space.title,
        summary=f"User '{instance.creator.username}' created a quiz named '{instance.title}' in the space '{instance.space.title}', on '{datetime.today().strftime('%d/%m/%Y, %H:%M:%S')}'",
        type='create_quiz',
        actor=instance.creator.username,
        object=instance.description,
        published=datetime.today().strftime('%d/%m/%Y, %H:%M:%S'),
    )

    activity_data_json = crt_qz_activity.dict_creator()

    ActivityStreamModel.objects.create(activity=activity_data_json)

    print(activity_data_json)


@receiver(post_save, sender=ResourceModel)
def on_create_step(sender, instance, **kwargs):

    crt_rsc_activity = MyActivity(
        context=instance.resourcespace.title,
        summary=f"User '{instance.resourcecreator.username}' created a resource named '{instance.resourcename}' in the space '{instance.resourcespace.title}', on '{datetime.today().strftime('%d/%m/%Y, %H:%M:%S')}'",
        type='create_resource',
        actor=instance.resourcecreator.username,
        object={
            'resource_info':  instance.resourceinfo,
            'resource_attachment':  instance.resourceattachment.name,
        },
        #published=instance.created_time.strftime('%d/%m/%Y, %H:%M:%S'),
        published=datetime.today().strftime('%d/%m/%Y, %H:%M:%S'),
    )

    activity_data_json = crt_rsc_activity.dict_creator()

    ActivityStreamModel.objects.create(activity=activity_data_json)

    print(activity_data_json)
