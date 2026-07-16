#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#  #
#    http://www.apache.org/licenses/LICENSE-2.0
#  #
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.
from __future__ import annotations

import logging

from pydantic import Field

from pyiceberg.io import FileIO
from pyiceberg.typedef import Identifier
from pyiceberg.view import ViewMetadata

logger = logging.getLogger(__name__)

METADATA_FOLDER_NAME = "metadata"


class BaseViewOperations:
    _identifier: Identifier = Field()
    current_metadata: ViewMetadata
    current_metadata_location: str = Field()
    io: FileIO
    should_refresh: bool = Field(default=True)
    version: int = Field(default=-1)

    def __init__(
        self, *,
        identifier: Identifier,
        metadata: ViewMetadata,
        current_metadata: ViewMetadata,
        current_metadata_location: str,
        io: FileIO,
        should_refresh: bool,
        version: int,
    ):
        self.identifier = identifier
        self.metadata = metadata
        self.current_metadata = current_metadata
        self.current_metadata_location = current_metadata_location
        self.io = io
        self.should_refresh = should_refresh
        self.version = version

    def view_name(self) -> Identifier:
        return self._identifier

    def current_version(self) -> int:
        return self.version

    def current_location(self) -> str:
        return self.current_metadata_location

    def current(self) -> ViewMetadata:
        return self.current_metadata

    def refresh(self) -> BaseViewOperations:
        ...

    def commit(self):
        ...

    def write_new_metadata(self):
        ...

    def write_new_metadata_if_required(self):
        ...

    def new_metadata_file_path(self):
        ...

    def metadata_file_location(self):
        ...

    def refresh_from_metadata_location(self):
        ...

    def parse_version(self):
        ...
