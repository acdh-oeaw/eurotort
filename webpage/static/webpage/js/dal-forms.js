(function () {
	function normalizeText(value) {
		return (value || "").replace(/\s+/g, " ").trim();
	}

	function getLabelText(element) {
		if (!element || !element.id) {
			return "";
		}
		var label = document.querySelector('label[for="' + element.id + '"]');
		return label ? normalizeText(label.textContent) : "";
	}

	function setAriaLabelIfMissing(element, label) {
		if (!element || !label || element.hasAttribute("aria-label")) {
			return;
		}
		element.setAttribute("aria-label", label);
	}

	function applySelect2AccessibleName(selectElement) {
		if (!selectElement || !selectElement.classList.contains("select2-hidden-accessible")) {
			return;
		}

		var labelText = getLabelText(selectElement);
		if (!labelText) {
			return;
		}

		setAriaLabelIfMissing(selectElement, labelText);

		var container = selectElement.nextElementSibling;
		if (!container || !container.classList.contains("select2")) {
			return;
		}

		var selection = container.querySelector(".select2-selection");
		setAriaLabelIfMissing(selection, labelText);

		container
			.querySelectorAll(".select2-search__field")
			.forEach(function (searchField) {
				setAriaLabelIfMissing(searchField, labelText + " search");
			});
	}

	function applyAllSelect2AccessibleNames() {
		document
			.querySelectorAll("select.select2-hidden-accessible")
			.forEach(applySelect2AccessibleName);
	}

	function applyOpenSelect2SearchLabel() {
		var openContainer = document.querySelector(".select2.select2-container--open");
		if (!openContainer) {
			return;
		}

		var linkedSelect = openContainer.previousElementSibling;
		if (!linkedSelect || linkedSelect.tagName !== "SELECT") {
			return;
		}

		var labelText = getLabelText(linkedSelect);
		if (!labelText) {
			return;
		}

		document
			.querySelectorAll(".select2-container--open .select2-search__field")
			.forEach(function (searchField) {
				setAriaLabelIfMissing(searchField, labelText + " search");
			});
	}

	function applyDateRangeAccessibleNames() {
		document
			.querySelectorAll('input[id$="_0"], input[id$="_1"]')
			.forEach(function (inputElement) {
				if (inputElement.hasAttribute("aria-label")) {
					return;
				}

				var baseId = inputElement.id.replace(/_(0|1)$/, "");
				var suffix = inputElement.id.endsWith("_0") ? "start" : "end";
				var baseLabel = "";

				var directLabel = document.querySelector('label[for="' + baseId + '"]');
				if (directLabel) {
					baseLabel = normalizeText(directLabel.textContent);
				}

				if (!baseLabel) {
					var fieldWrapper = inputElement.closest("fieldset, .mb-3, .form-group");
					if (fieldWrapper) {
						var wrapperLabel = fieldWrapper.querySelector("legend, .form-label");
						if (wrapperLabel) {
							baseLabel = normalizeText(wrapperLabel.textContent);
						}
					}
				}

				if (baseLabel) {
					inputElement.setAttribute("aria-label", baseLabel + " " + suffix);
				}
			});
	}

	function refreshAccessibilityLabels() {
		applyAllSelect2AccessibleNames();
		applyOpenSelect2SearchLabel();
		applyDateRangeAccessibleNames();
	}

	function setupMutationObserver() {
		var observer = new MutationObserver(function (mutations) {
			var shouldRefresh = mutations.some(function (mutation) {
				if (mutation.type === "childList") {
					return mutation.addedNodes.length > 0;
				}
				if (mutation.type === "attributes") {
					return mutation.attributeName === "class";
				}
				return false;
			});

			if (shouldRefresh) {
				refreshAccessibilityLabels();
			}
		});

		observer.observe(document.body, {
			subtree: true,
			childList: true,
			attributes: true,
			attributeFilter: ["class"],
		});
	}

	document.addEventListener("DOMContentLoaded", function () {
		refreshAccessibilityLabels();
		setupMutationObserver();

		// DAL may emit a custom event when widgets are initialized.
		document.addEventListener("dal-element-initialized", refreshAccessibilityLabels);
	});
})();
