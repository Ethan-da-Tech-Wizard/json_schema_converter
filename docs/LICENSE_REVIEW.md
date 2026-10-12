# License review — Universal JSON Schema Converter

Reviewed 2026-10-12. Original project code retains **MIT** terms in [LICENSE](../LICENSE).

The owner selected MIT for previously unlicensed original code. Existing licenses were preserved. This choice does not relicense copied code, dependencies, datasets, model weights, fonts, logos, or game assets.

## Preserved notices

- [LICENSE](../LICENSE)

## Dependency evidence

[DEPENDENCIES.csv](DEPENDENCIES.csv) lists 13 manifest and lockfile records. Repeated packages can appear under different manifests, versions, or development scopes. Registry metadata is evidence, not a replacement for the actual license text. For unpinned ranges, `metadata_version` is the version inspected and is not a claim about every install. Go and system/build tools can require notices beyond package-manager metadata.

| Component | Declared version | License evidence |
| --- | --- | --- |
| npm: @types/node | 18.x | [MIT](https://registry.npmjs.org/%40types%2Fnode/latest) |
| npm: @types/vscode | ^1.80.0 | [MIT](https://registry.npmjs.org/%40types%2Fvscode/latest) |
| npm: typescript | ^5.1.3 | [Apache-2.0](https://registry.npmjs.org/typescript/latest) |
| PyPI: genson | >=1.2.2 | [MIT](https://pypi.org/pypi/genson/json) |
| PyPI: pandas | >=2.0.0 | [OSI Approved :: BSD License](https://pypi.org/pypi/pandas/json) |
| PyPI: xmltodict | >=0.13.0 | [MIT](https://pypi.org/pypi/xmltodict/json) |
| PyPI: PyYAML | >=6.0 | [MIT](https://pypi.org/pypi/PyYAML/json) |
| PyPI: openpyxl | >=3.1.0 | [MIT](https://pypi.org/pypi/openpyxl/json) |
| PyPI: pathlib | >=1.0.1 | [MIT License](https://pypi.org/pypi/pathlib/json) |

## Project-specific considerations

Python parsers and the editor extension share the schema-inference engine. Install the declared Python requirements before using the CLI.

## Remaining work before binary distribution

No unresolved registry-license lookup remains in the listed package records. System packages, downloaded tools/models, optional plugins, release binaries, and externally obtained assets need a build-specific inventory. This source review is not a blanket legal certification or a claim that every release artifact has been audited.
