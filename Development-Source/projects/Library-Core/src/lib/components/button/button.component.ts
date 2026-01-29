import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ButtonModule } from 'primeng/button';

/**
 * WB Button Component
 * 
 * A customizable button component built on PrimeNG with design token styling.
 * Supports multiple variants, sizes, and states.
 * 
 * @example
 * ```html
 * <wb-button label="Click me" variant="primary" size="md"></wb-button>
 * ```
 */
@Component({
  selector: 'wb-button',
  standalone: true,
  imports: [CommonModule, ButtonModule],
  templateUrl: './button.component.html',
  styleUrl: './button.component.scss'
})
export class ButtonComponent {
  /**
   * Button label text
   */
  @Input() label: string = 'Button';

  /**
   * Button variant style
   */
  @Input() variant: 'primary' | 'secondary-gray' | 'tertiary-gray' | 'danger' | 'link-color' | 'link-gray' = 'primary';

  /**
   * Button size
   */
  @Input() size: 'xs' | 'sm' | 'md' | 'lg' = 'md';

  /**
   * Disabled state
   */
  @Input() disabled: boolean = false;

  /**
   * Loading state
   */
  @Input() loading: boolean = false;

  /**
   * Leading icon class (e.g., 'pi pi-plus')
   */
  @Input() leadingIcon?: string;

  /**
   * Whether to show the leading icon
   */
  @Input() showLeadingIcon: boolean = false;

  /**
   * Trailing icon class (e.g., 'pi pi-arrow-right')
   */
  @Input() trailingIcon?: string;

  /**
   * Whether to show the trailing icon
   */
  @Input() showTrailingIcon: boolean = false;

  /**
   * Icon Only mode (renders as a square, hides label)
   */
  @Input() iconOnly: boolean = false;

  /**
   * The icon class to use in Icon Only mode
   */
  @Input() icon?: string;

  /**
   * Full width button
   */
  @Input() fullWidth: boolean = false;
}
