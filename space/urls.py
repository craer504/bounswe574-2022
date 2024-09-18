from django.urls import path

from space.views.mycreatedspaces import mycreatedspaces
from .views import (
    update_resource,
    homepage,
    signout,
    spaces,
    aboutus,
    mycreatedspaces,
    mymemberspaces,
    spacedetails,
    create_space,
    create_message,
    warning,
    create_step,
    update_space,
    delete_space,
    signout,
    change_password,
    create_term,
    edit_profile,
    register,
    create_content,
    content_relations,
    display_contents,
    delete_content,
    resource,
    display_resource,
    display_step,
    display_members,
    edit_profile1,
    quiz_section,
    resource_section,
    discussion_section,
    learning_section,
    glossary_section,
    graph_section
)
from .views import delete_resource
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", homepage, name="homepage"),
    path("spaces", spaces, name="spaces"),
    path("aboutus", aboutus, name="aboutus"),
    path("warning", warning, name="warning"),
    path("mycreatedspaces", mycreatedspaces, name="mycreatedspaces"),
    path("mymemberspaces", mymemberspaces, name="mymemberspaces"),
    path("spacedetails/<slug:slug>", spacedetails, name="spacedetails"),
    path("create-space", create_space, name="create-space"),
    path("create-message/<slug:slug>", create_message, name="create-message"),
    path("create-term/<slug:slug>", create_term, name="create-term"),
    path("create-step/<slug:slug>", create_step, name="create-step"),
    path("display-step/<slug:slug>/<int:id>", display_step, name="display-step"),
    path(
        "display-members/<slug:slug>/<int:id>", display_members, name="display-members"
    ),
    path("resource/<slug:slug>", resource, name="resource"),
    path(
        "update-resource/<slug:slug>/<int:id>", update_resource, name="update-resource"
    ),
    path(
        "delete-resource/<slug:slug>/<int:id>", delete_resource, name="delete-resource"
    ),
    path("update-space/<slug:slug>", update_space, name="update-space"),
    path("delete-space/<slug:slug>", delete_space, name="delete-space"),
    path("signout", signout, name="signout"),
    path("change-password", change_password, name="change-password"),
    path("edit-profile", edit_profile, name="edit-profile"),
    path("edit-profile1", edit_profile1, name="edit-profile1"),
    path("register", register, name="register"),
    path(
        "signin",
        auth_views.LoginView.as_view(template_name="pages/signin.html"),
        name="signin",
    ),
    path(
        "spacedetails/<slug:slug>/create-content", create_content, name="create-content"
    ),
    path(
        "spacedetails/<slug:slug>/edit-content/<int:content_id>",
        create_content,
        name="edit-content",
    ),
    path(
        "spacedetails/<slug:slug>/content", content_relations, name="content-relations"
    ),
    path(
        "spacedetails/<slug:slug>/display-contents",
        display_contents,
        name="display-contents",
    ),
    path(
        "spacedetails/<slug:slug>/delete-content/<int:id>",
        delete_content,
        name="delete-content",
    ),
    path("resource/<slug:slug>/<int:id>", display_resource, name="display-resource"),
    path("quizsection/<slug:slug>", quiz_section, name="quiz_section"),
    path("resourcesection/<slug:slug>", resource_section, name="resource_section"),
    path("discussionsection/<slug:slug>", discussion_section, name="discussion_section"),
    path("learningsection/<slug:slug>", learning_section, name="learning_section"),
    path("glossarysection/<slug:slug>", glossary_section, name="glossary_section"),
    path("graphsection/<slug:slug>", graph_section, name="graph_section"),
]
