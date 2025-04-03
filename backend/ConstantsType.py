class ConstantsBaseMeta(type):
    def __new__(cls, typename, bases, ns):
        fields = ns.get('__annotations__', {})

        for k, v in fields.items():
            if k not in ns:
                raise ValueError(f"Constant '{k}' must have a value")

        ns['__slots__'] = tuple(fields)
        ns['__new__'] = cls.__new_class

        return super().__new__(cls, typename, bases, ns)

    def __new_class(cls):
        raise TypeError("Cannot instantiate Constants class")

    @property
    def __dict__(self):
        base_dict = super().__dict__
        return {k: v for k, v in base_dict.items() if not k.startswith('__')}

    def keys(cls):
        return cls.__dict__.keys()

    def values(cls):
        return cls.__dict__.values()

    def items(cls):
        return cls.__dict__.items()

    def get(cls, key, default=None):
        return cls.__dict__.get(key, default)

    def __getitem__(self, item):
        return self.__dict__.get(item)

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return f"<{self.__name__} {self.__dict__}>"

    def __setattr__(self, key, value):
        raise TypeError(f"Cannot modify constant '{key}' in {self.__name__}")

    def __delattr__(self, item):
        raise TypeError(f"Cannot delete constant '{item} in {self.__name__}")


class ConstantsBase(metaclass=ConstantsBaseMeta):
    pass
