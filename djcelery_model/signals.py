import django.dispatch

post_update = django.dispatch.Signal(providing_args=["sender", "task_id", "count", "update_kwargs"])
