import type { Meta, StoryObj } from '@storybook/angular';
import { ButtonComponent } from './button.component';

const meta: Meta<ButtonComponent> = {
    title: 'Components/Button',
    component: ButtonComponent,
    tags: ['autodocs'],
    argTypes: {
        label: {
            control: 'text',
            table: { category: 'General' }
        },
        variant: {
            control: 'select',
            options: ['primary', 'secondary-gray', 'tertiary-gray', 'danger', 'link-color', 'link-gray'],
            table: { category: 'General' }
        },
        size: {
            control: 'select',
            options: ['xs', 'sm', 'md', 'lg'],
            table: { category: 'General' }
        },
        iconOnly: {
            control: 'boolean',
            table: { category: 'Icons' }
        },
        icon: {
            control: 'text',
            table: { category: 'Icons' }
        },
        showLeadingIcon: {
            control: 'boolean',
            table: { category: 'Icons' }
        },
        leadingIcon: {
            control: 'text',
            table: { category: 'Icons' }
        },
        showTrailingIcon: {
            control: 'boolean',
            table: { category: 'Icons' }
        },
        trailingIcon: {
            control: 'text',
            table: { category: 'Icons' }
        },
        disabled: {
            control: 'boolean',
            table: { category: 'States' }
        },
        loading: {
            control: 'boolean',
            table: { category: 'States' }
        },
        fullWidth: {
            control: 'boolean',
            table: { category: 'States' }
        },
    },
    args: {
        label: 'Button',
        variant: 'primary',
        size: 'md',
        showLeadingIcon: true,
        leadingIcon: 'pi pi-plus',
        showTrailingIcon: false,
        trailingIcon: 'pi pi-arrow-right',
        iconOnly: false,
        icon: 'pi pi-plus',
        disabled: false,
        loading: false,
        fullWidth: false,
    },
};

export default meta;
type Story = StoryObj<ButtonComponent>;

export const Primary: Story = {
    args: {
        label: 'Primary Button',
        variant: 'primary',
        size: 'md',
    },
};

export const SecondaryGray: Story = {
    name: 'Secondary Gray',
    args: {
        label: 'Secondary Gray',
        variant: 'secondary-gray',
        size: 'md',
    },
};

export const TertiaryGray: Story = {
    name: 'Tertiary Gray',
    args: {
        label: 'Tertiary Gray',
        variant: 'tertiary-gray',
        size: 'md',
    },
};

export const LinkColor: Story = {
    name: 'Link Color',
    args: {
        label: 'Link Color',
        variant: 'link-color',
        size: 'md',
    },
};

export const LinkGray: Story = {
    name: 'Link Gray',
    args: {
        label: 'Link Gray',
        variant: 'link-gray',
        size: 'md',
    },
};

export const Danger: Story = {
    args: {
        label: 'Danger Button',
        variant: 'danger',
        size: 'md',
    },
};

export const WithIcons: Story = {
    name: 'With Icons',
    args: {
        label: 'Icons Toggled',
        variant: 'secondary-gray',
        size: 'md',
        leadingIcon: 'pi pi-plus',
        showLeadingIcon: true,
    },
};

export const IconOnly: Story = {
    name: 'Icon Only',
    args: {
        icon: 'pi pi-search',
        iconOnly: true,
        variant: 'primary',
        size: 'md'
    },
};

export const Sizes: Story = {
    render: (args) => ({
        props: args,
        template: `
      <div style="display: flex; flex-direction: column; gap: 16px; align-items: flex-start;">
        <wb-button label="Size LG" size="lg" variant="primary"></wb-button>
        <wb-button label="Size MD" size="md" variant="primary"></wb-button>
        <wb-button label="Size SM" size="sm" variant="primary"></wb-button>
        <wb-button label="Size XS" size="xs" variant="primary"></wb-button>
      </div>
    `,
    }),
};

export const Loading: Story = {
    args: {
        label: 'Submitting...',
        loading: true,
        variant: 'primary'
    },
};

export const Disabled: Story = {
    args: {
        label: 'Disabled Button',
        disabled: true,
        variant: 'primary'
    },
};
