"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
*!
Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class PageProfile(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMANDS_FIELD_NUMBER: builtins.int
    EXEC_TIME_FIELD_NUMBER: builtins.int
    PREP_TIME_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    UNCAUGHT_EXCEPTION_FIELD_NUMBER: builtins.int
    ATTRIBUTIONS_FIELD_NUMBER: builtins.int
    OS_FIELD_NUMBER: builtins.int
    TIMEZONE_FIELD_NUMBER: builtins.int
    HEADLESS_FIELD_NUMBER: builtins.int
    IS_FRAGMENT_RUN_FIELD_NUMBER: builtins.int
    exec_time: builtins.int
    prep_time: builtins.int
    uncaught_exception: builtins.str
    os: builtins.str
    timezone: builtins.str
    headless: builtins.bool
    is_fragment_run: builtins.bool
    @property
    def commands(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Command]: ...
    @property
    def config(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def attributions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        commands: collections.abc.Iterable[global___Command] | None = ...,
        exec_time: builtins.int = ...,
        prep_time: builtins.int = ...,
        config: collections.abc.Iterable[builtins.str] | None = ...,
        uncaught_exception: builtins.str = ...,
        attributions: collections.abc.Iterable[builtins.str] | None = ...,
        os: builtins.str = ...,
        timezone: builtins.str = ...,
        headless: builtins.bool = ...,
        is_fragment_run: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["attributions", b"attributions", "commands", b"commands", "config", b"config", "exec_time", b"exec_time", "headless", b"headless", "is_fragment_run", b"is_fragment_run", "os", b"os", "prep_time", b"prep_time", "timezone", b"timezone", "uncaught_exception", b"uncaught_exception"]) -> None: ...

global___PageProfile = PageProfile

@typing.final
class Argument(google.protobuf.message.Message):
    """The field names are used as part of the event json sent
    to Segment. Since there is a 32kb limit for the event
    size we are using short names to optimize for the size.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    K_FIELD_NUMBER: builtins.int
    T_FIELD_NUMBER: builtins.int
    M_FIELD_NUMBER: builtins.int
    P_FIELD_NUMBER: builtins.int
    k: builtins.str
    """The keyword of the argument:"""
    t: builtins.str
    """The type of the argument:"""
    m: builtins.str
    """Some metadata about the argument value:"""
    p: builtins.int
    """Contains the position (if positional argument):"""
    def __init__(
        self,
        *,
        k: builtins.str = ...,
        t: builtins.str = ...,
        m: builtins.str = ...,
        p: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["k", b"k", "m", b"m", "p", b"p", "t", b"t"]) -> None: ...

global___Argument = Argument

@typing.final
class Command(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    name: builtins.str
    time: builtins.int
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Argument]: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        args: collections.abc.Iterable[global___Argument] | None = ...,
        time: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["args", b"args", "name", b"name", "time", b"time"]) -> None: ...

global___Command = Command
