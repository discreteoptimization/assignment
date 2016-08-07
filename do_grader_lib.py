from collections import namedtuple

GraderMetadata = namedtuple("GraderMetadata", ['url', 'name', 'sense', 'part_data', 'quality_data'])
Part = namedtuple("Part", ['id', 'input_file', 'solver_file', 'name'])
PartQuality = namedtuple("PartQuality", ['id', 'pt3', 'pt10'])
