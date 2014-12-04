from django.template.response import TemplateResponse
import electronics.labeler

def print_labels(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    app_label = opts.app_label

    if request.POST.get('post'):
        used = [(map(int, v.split(','))) for v in request.POST.getlist('used')]
        labels = sum([obj.to_label_values() for obj in queryset], [])
        electronics.labeler.write_labels(labels, used)
        return

    if len(queryset) == 1:
        objects_name = opts.verbose_name
    else:
        objects_name = opts.verbose_name_plural

    context = {
        "title": "Print labels",
        "objects_name": objects_name,
        'queryset': queryset,
        "opts": opts,
        'xrange': range(1, 6),
        'yrange': range(1, 14),
    }

    # Display the confirmation page
    return TemplateResponse(request, "admin/print_labels.html",
                            context, current_app=modeladmin.admin_site.name)
