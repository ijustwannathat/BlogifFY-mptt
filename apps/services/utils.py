from pytils.translit import slugify
from uuid import uuid4

def unique_slugify(instance, slug, slug_field):
    model = instance.__class__
    unique_slug = slug_field
    instance_case = model.objects.filter(slug=slug_field)
    if not slug_field:
        unique_slug = slugify(slug)
    elif instance_case and instance_case.last().id != instance.id:
        unique_slug = f'{slugify(slug)}-{uuid4().hex[:8]}'
    return unique_slug

