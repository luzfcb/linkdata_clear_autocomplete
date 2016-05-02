from dal import autocomplete


class ForwardExtrasMixin(object):
    def __init__(self, url=None, forward=None, unselect_if_forward_changed=None, *args, **kwargs):
        self.unselect_if_forward_changed = unselect_if_forward_changed
        super(ForwardExtrasMixin, self).__init__(url, forward, *args, **kwargs)

    def build_attrs(self, *args, **kwargs):
        attrs = super(ForwardExtrasMixin, self).build_attrs(*args, **kwargs)

        if self.unselect_if_forward_changed is not None and self.forward is not None:
            values = set(self.unselect_if_forward_changed).intersection(self.forward)
            if values:
                attrs.setdefault('data-autocomplete-light-unselect-if-forward-changed',
                                 ','.join(values))
        return attrs

    class Media:
        """Automatically include static files for the admin."""

        js = (
            'autocomplete_light/select2forwardextras.js',
        )


class ModelSelect2ForwardExtras(ForwardExtrasMixin, autocomplete.ModelSelect2):
    pass


class ModelSelect2MultipleForwardExtras(ForwardExtrasMixin, autocomplete.ModelSelect2Multiple):
    pass
